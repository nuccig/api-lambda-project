from chalice import Chalice

app = Chalice(app_name="customers")

# Simulação de um banco de dados em memória
users = {
    "users": [
        {"name": "usuário1", "phone": "47999999999"},
        {"name": "usuário2", "phone": "47999999999"},
        {"name": "usuário3", "phone": "47999999999"},
    ]
}


companies = {
    "companies": [
        {"name": "empresa1", "telefone": "47999999999"},
        {"name": "empresa2", "telefone": "47999999999"},
        {"name": "empresa3", "telefone": "47999999999"},
    ]
}


# Criação de rotas para usuários de PF
@app.route("/customers/person", methods=["POST"])
def create_user():
    requests_params = app.current_request.json_body

    response = {
        "statusCode": 201,
        "body": f"Usuário {requests_params['name']} criado com sucesso!",
    }

    return response


@app.route("/customers/person", methods=["PUT"])
def update_user():
    requests_params = app.current_request.json_body

    if "name" not in requests_params or "phone" not in requests_params:
        return {
            "statusCode": 400,
            "body": "Parâmetros 'name' e 'phone' são obrigatórios.",
        }
    if not isinstance(requests_params["name"], str) or not isinstance(
        requests_params["phone"], int
    ):
        return {
            "statusCode": 400,
            "body": "Parâmetros 'name' e 'phone' devem ser do tipo string e integer, respectivamente.",
        }
    if len(requests_params["name"]) < 3 or len(str(requests_params["phone"])) < 10:
        return {
            "statusCode": 400,
            "body": "Parâmetros 'name' e 'phone' devem ter pelo menos 3 e 10 caracteres, respectivamente.",
        }

    matches = [u for u in users["users"] if u["name"] == requests_params["name"]]
    user = matches[0] if matches else None

    if user:
        user["phone"] = requests_params["phone"]
        return {
            "statusCode": 200,
            "body": f"Usuário {requests_params['name']} atualizado com sucesso!",
        }
    else:
        return {
            "statusCode": 404,
            "body": f"Usuário {requests_params['name']} não encontrado.",
        }


@app.route("/customers/person", methods=["DELETE"])
def delete_user():
    requests_params = app.current_request.json_body

    if "name" not in requests_params:
        return {"statusCode": 400, "body": "Parâmetro 'name' é obrigatório."}

    matches = [u for u in users["users"] if u["name"] == requests_params["name"]]
    user = matches[0] if matches else None

    if user:
        users["users"].remove(user)
        return {
            "statusCode": 200,
            "body": f"Usuário {requests_params['name']} deletado com sucesso!",
        }
    else:
        return {
            "statusCode": 404,
            "body": f"Usuário {requests_params['name']} não encontrado.",
        }


@app.route("/customers/person/{name}", methods=["GET"])
def get_user(name):
    matches = [u for u in users["users"] if u["name"] == name]
    if matches:
        return {"statusCode": 200, "body": matches[0]}
    else:
        return {"statusCode": 404, "body": f"Usuário {name} não encontrado."}


@app.route("/customers/persons", methods=["GET"])
def get_persons():
    response = {"statusCode": 200, "body": users}
    return response


# Criação de rotas para usuários de PJ
@app.route("/customers/company", methods=["POST"])
def create_company():
    requests_params = app.current_request.json_body

    response = {
        "statusCode": 201,
        "body": f"Empresa {requests_params['name']} criado com sucesso!",
    }

    return response


@app.route("/customers/company", methods=["PUT"])
def update_company():
    requests_params = app.current_request.json_body

    if "name" not in requests_params or "telefone" not in requests_params:
        return {
            "statusCode": 400,
            "body": "Parâmetros 'name' e 'telefone' são obrigatórios.",
        }
    if not isinstance(requests_params["name"], str) or not isinstance(
        requests_params["telefone"], int
    ):
        return {
            "statusCode": 400,
            "body": "Parâmetros 'name' e 'telefone' devem ser do tipo string e integer, respectivamente.",
        }
    if len(requests_params["name"]) < 3 or len(str(requests_params["telefone"])) < 10:
        return {
            "statusCode": 400,
            "body": "Parâmetros 'name' e 'telefone' devem ter pelo menos 3 e 10 caracteres, respectivamente.",
        }

    matches = [u for u in users["users"] if u["name"] == requests_params["name"]]
    user = matches[0] if matches else None

    if user:
        user["telefone"] = requests_params["telefone"]
        return {
            "statusCode": 200,
            "body": f"Empresa {requests_params['name']} atualizado com sucesso!",
        }
    else:
        return {
            "statusCode": 404,
            "body": f"Empresa {requests_params['name']} não encontrado.",
        }


@app.route("/customers/company", methods=["DELETE"])
def delete_company():
    requests_params = app.current_request.json_body

    if "name" not in requests_params:
        return {"statusCode": 400, "body": "Parâmetro 'name' é obrigatório."}

    matches = [u for u in users["users"] if u["name"] == requests_params["name"]]
    user = matches[0] if matches else None

    if user:
        users["users"].remove(user)
        return {
            "statusCode": 200,
            "body": f"Empresa {requests_params['name']} deletado com sucesso!",
        }
    else:
        return {
            "statusCode": 404,
            "body": f"Empresa {requests_params['name']} não encontrado.",
        }


@app.route("/customers/companies", methods=["GET"])
def get_companies():
    response = {"statusCode": 200, "body": users}
    return response


@app.route("/customers/company/{name}", methods=["GET"])
def get_company(name):
    matches = [u for u in users["users"] if u["name"] == name]
    if matches:
        return {"statusCode": 200, "body": matches[0]}
    else:
        return {"statusCode": 404, "body": f"Empresa {name} não encontrada."}
