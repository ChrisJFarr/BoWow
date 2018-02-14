from flask_api import FlaskAPI
try:  # Avoid IDE error highlighting :-|
    from robot_drive import RobotDrive
except ImportError:
    from ..robot_drive.robot_drive import RobotDrive


app = FlaskAPI(__name__)


# API for passing controls to RobotDrive instance
@app.route("/drive/<code>", methods=['GET'])
def notes_list(code):
    # Code list object len 4
    code = [int(b) for b in code]
    robot.codeControl(code)
    return "driving"


if __name__ == "__main__":
    robot = RobotDrive()
    print("running")
    app.run(host="0.0.0.0", port=5000, debug=False)  # Can't debug w/ serial connect
