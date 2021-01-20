Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@anhthiencao 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


anhthiencao
/
github-demo-anhthien
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
github-demo-anhthien/main.py /

Thien Nguyen Add main.py file
Latest commit f1aef5c 20 minutes ago
 History
 0 contributors
50 lines (35 sloc)  1.34 KB
  
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, validate
import jwt

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    class ActivitiesSchema(Schema):
        id = fields.Int()
        direction = fields.Str(required=True)
        type = fields.Str(required=True)
        title = fields.Str(required=True)
        var = fields.Str(required=True)
        args = fields.Str(required=True)


    class StepsSchema(Schema):
        id = fields.Int()
        title = fields.Str()
        activities = fields.List(fields.Nested(ActivitiesSchema), required=True)
        allow_changes = fields.Bool(required=True)
        allow_return = fields.Bool(required=True)

    
    class WorkflowSchema(Schema):
        id = fields.Int()
        name = fields.Str(required=True)
        steps = fields.List(fields.Nested(StepsSchema), many=True)

    data = request.get_json()

    step_list = data["steps"]
    if len(step_list):
        for num_step, step in enumerate(step_list):
            step["id"] = num_step + 1

            if len(step["activities"]):
                for num_act, act in enumerate(step["activities"]):
                    act["id"] = num_act + 1
    
    result = WorkflowSchema().load(data)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.2")

© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
