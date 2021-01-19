from app import app
from flask import jsonify, request
import json
import os
from os import listdir
from marshmallow import Schema, fields, validate
import jwt

API_ROOT = f'/template'
WORKFLOW_DIR = os.path.join(os.path.dirname(__file__), '..', 'workflows')


class ActivitiesSchema(Schema):
    id = fields.Int(required=True)
    direction = fields.Str(
        required=True,
        validate=validate.Length(min=1)
    )
    type = fields.Str(
        required=True,
        validate=validate.Length(min=1)
    )
    title = fields.Str(
        required=True,
        validate=validate.Length(min=1)
    )
    var = fields.Str(
        required=True,
        validate=validate.Length(min=1)
    )
    args = fields.Str(required=True)


class StepsSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(
        required=True,
        validate=validate.Length(min=1)
    )
    activities = fields.List(
        fields.Nested(ActivitiesSchema),
        required=True
    )
    allow_changes = fields.Bool(required=True)
    allow_return = fields.Bool(required=True)


class WorkflowSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    steps = fields.List(
        fields.Nested(StepsSchema),
        required=True
    )
    delete = fields.Bool(required=True)
    class Meta:
        ordered = True


def access_authorization():
    """Check user"""
    auth = request.headers.get('Authorization')
    if auth is not None and auth.startswith('Bearer '):
        segment_2 = auth.split(' ')[1]
        decode = jwt.decode(segment_2, "go-rbac-secret-key", algorithms=["HS256"])
        if decode["Role"] == "admin" or decode["Role"] == "manager":
            return True
        else:
            return False
   
    return "<h1>403: User is not allowed</h1>"


@app.route(f'{API_ROOT}/workflows', methods=["GET"])
def get_all_workflows():
    """"Get all workflows"""
    if access_authorization() is True:
        data = {}
        for wf in listdir(WORKFLOW_DIR):
            with open(f"{WORKFLOW_DIR}\{wf}", "r") as f:
                result = json.load(f)
                if result["delete"] == False:
                    name = wf.rsplit('.', 1)[0]
                    data[name] = result
                    del data[name]["delete"]

        return jsonify(data)

    return "<h1>403: User is not allowed</h1>"


@app.route(f'{API_ROOT}/workflows/<id>', methods=["GET"])
def get_workflow(id):
    """"Get workflows by id"""
    if access_authorization() is True:
        for wf in listdir(WORKFLOW_DIR):
            if wf.startswith(f"{id}"):
                with open(f"{WORKFLOW_DIR}\{wf}", "r") as f:
                    data = json.load(f)
                del data["delete"]

                return jsonify(data)

    return "<h1>403: User is not allowed</h1>"


@app.route(f'{API_ROOT}/workflows/<id>', methods=["DELETE"])
def delete_workflow(id):
    """"Delete workflows by id"""
    if access_authorization() is True:
        for wf in listdir(WORKFLOW_DIR):
            if wf.startswith(f"{id}"):
                with open(f"{WORKFLOW_DIR}\{wf}", "r") as f:
                    data = json.load(f)
                    data["delete"] = True
                with open(f"{WORKFLOW_DIR}\{wf}", "w") as f:
                    json.dump(data, f)
                    f.close()
                del data["delete"]

                return jsonify(data)

    return "<h1>403: User is not allowed</h1>"


@app.route(f'{API_ROOT}/workflows/recover/<id>', methods=["PUT"])
def recover_workflow(id):
    """"Recover deleted workflows"""
    for wf in listdir(WORKFLOW_DIR):
        if wf.startswith(f"{id}"):
            with open(f"{WORKFLOW_DIR}\{wf}", "r") as f:
                data = json.load(f)
            if data["delete"] == True:
                data["delete"] = False

                with open(f"{WORKFLOW_DIR}\{wf}", "w") as f:
                    json.dump(data, f)
                    f.close()
                del data["delete"]

                return jsonify(data)
            else:
                return "This workflow is not deleted"

    return "<h1>403: User is not allowed</h1>"


@app.route(f'{API_ROOT}/workflows/new', methods=["POST"])
def post_new_wf():
    """"Add new workflow """
    if access_authorization() is True:
        totalFile = len(listdir(WORKFLOW_DIR))

        data = request.get_json()
        data["delete"] = False
        data["id"] = totalFile + 1
        
        step_list = data["steps"]
        if len(step_list):
            for num_step, step in enumerate(step_list):
                step["id"] = num_step + 1

                if len(step["activities"]):
                    for num_act, act in enumerate(step["activities"]):
                        act["id"] = num_act + 1

        result = WorkflowSchema().load(data)
        filename = "_".join((result["name"]).split())

        with open(f"{WORKFLOW_DIR}\{totalFile + 1}_{filename}.json", "w") as f:
            f.close()
        with open(f"{WORKFLOW_DIR}\{totalFile + 1}_{filename}.json", "w") as f:
            f.write(json.dumps(result))
            f.close()
        result.pop("delete")

        return jsonify(result)
    
    return "<h1>403: User is not allowed</h1>"


@app.route(f'{API_ROOT}/workflows/<id>', methods=["PUT"])
def change_wf(id):
    """"Change workflows by id"""
    if access_authorization() is True:
        data = request.get_json()
        data["delete"] = False
        data["id"] = id

        result = WorkflowSchema().load(data)

        for wf in listdir(WORKFLOW_DIR):
            if wf.startswith(f"{id}"):
                with open(f"{WORKFLOW_DIR}\{wf}", "w") as f:
                    f.close()
                with open(f"{WORKFLOW_DIR}\{wf}", "w") as f:
                    f.write(json.dumps(result))
                    f.close()
                result.pop("delete")

                return jsonify(result)

    return "<h1>403: User is not allowed</h1>"


@app.route(f'{API_ROOT}/workflows/delete', methods=["GET"])
def get_deleted_workflows():
    """"Get deleted workflows"""
    if access_authorization() is True:
        data = {}
        for wf in listdir(WORKFLOW_DIR):
            with open(f"{WORKFLOW_DIR}\{wf}", "r") as f:
                result = json.load(f)
                if result["delete"] == True:
                    name = wf.rsplit('.', 1)[0]
                    data[name] = result
                    del data[name]["delete"]

        return json.dumps(data)

    return "<h1>403: User is not allowed</h1>"
