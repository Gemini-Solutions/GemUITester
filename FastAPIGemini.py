# This is flask api
from flask import Flask, request, jsonify
import gemini_pro_105
import gemini_LLM


app = Flask(__name__)

# This is known as creating route inside Flask
# '/' this is the initial route
@app.route("/")
def home():
    return "Home"

# For creating a "Get" route
# Anything written in <> in path are known as path parameters where we can pass values
# Query Parameters are the value enetered in the url after the '?' this returns the exact answer to the query value
@app.route("/get-user/")
def get_user():

    test_cases = gemini_LLM.unit_test_cases(
        ''' public Map<String, Object> loginUser(final User credentials) {
 
        String pass = credentials.getPassword();
        String username = credentials.getUsername().toLowerCase();
 
        Map<String, Object> data = new HashMap<>();
        User currentUser = userRepository.findByUsernameIgnoreCaseOrEmailIgnoreCase(username,username);
 
        if (currentUser == null || !pass.equalsIgnoreCase(currentUser.getPassword())) {
            log.info("Error occurred while trying to login for user: {}", credentials);
            throw new CustomException(currentUser == null ? USER_NOT_FOUND : INCORRECT_PASSWORD, HttpStatus.BAD_REQUEST);
        }
        if (Boolean.TRUE.equals(currentUser.getIsDeleted())) {
            data.put("token", "Login Failed");
            log.error("Error occurred while trying to login for user: {}", credentials);
            throw new CustomDataException(UNABLE_LOGIN_USER_BLOCKED, data, HttpStatus.UNAUTHORIZED);
        }
        if(!currentUser.getRealCompanyType().equalsIgnoreCase("VERIFIED")) {
            log.info("Error occurred while trying to login for user due to unverified company: {}", currentUser);
            throw new CustomException("Company verification still in progress. Please try again later !!", HttpStatus.UNAUTHORIZED);
 
        }
        String jwtToken = jwtHelperService.generateToken(currentUser.getUsername(), currentUser);
        data.put("token", jwtToken);
        data.put("username", currentUser.getUsername());
        data.put("firstName", currentUser.getFirstName());
        data.put("lastName", currentUser.getLastName());
 
        String companyName = currentUser.getRealCompanyType().equalsIgnoreCase("verified") ?
                currentUser.getRealCompany() : currentUser.getCompany();
        data.put("company", companyName);
        String userRole = UserRole.SUPER_ADMIN.toString().equals(currentUser.getRole()) ? UserRole.SUPER_ADMIN.toString() :
                currentUser.getRole();
        String role = currentUser.getRole() == null ? UserRole.USER.toString() : userRole;
 
        data.put("role", role);
        data.put("socket", role.equals(UserRole.SUPER_ADMIN.toString()) ? role : currentUser.getRealCompany());
 
        data.put("avatar", avatarUrl +
                currentUser.getFirstName() + " " + currentUser.getLastName());
 
        return data;
    } '''
    )

    user_data = {
        "code": "code",
        "name": "Sachin Sharma",
        "test_cases": test_cases
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


# For creating a POST request
# if request.method=="POST": This could also be used if we are not specifying it in route.
@app.route("/create-user", methods=["POST"])
def create_user():

    code = request.data.decode('utf-8')
    # test_cases = "These are the Generated UNIT TEST CASE: /n/n" + code
    test_cases = gemini_LLM.unit_test_cases(code)

    return jsonify({'test_cases': test_cases})


if __name__ == "__main__":
    app.run(debug=True)