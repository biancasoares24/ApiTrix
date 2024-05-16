import requests
import json


print("O que deseja fazer? Caso deseje executar requests de criação, escolha uma das opções abaixo: ")
action = input("CREATE OR DELETE: ")
if action == "CREATE":
    # URL da API
    url_organization = 'http://desafio-api-trix.trixlog.com/organization'

    # Solicitando entrada do usuário para o parâmetro "name"
    name_organization = input("Por favor, insira o nome da sua organização: ")
    description_organization = input("Por favor, insira a descrição da sua organização: ")

    # Dados para a requisição, com variáveis substituindo os valores
    organization = {
        "name": name_organization,
        "description": description_organization,
        "state": "",
        "country": "",
        "gmt": -180,
        "dst": False,
        "trixOrganization": False,
        "parentOrganization": {
            "id": 2,
            "name": "Brasil",
            "description": " Pai de Todos",
            "state": "",
            "country": "",
            "gmt": -180,
            "dst": False,
            "trixOrganization": False,
            "hierarchicalLevel": {
                "id": 2,
                "name": "País",
                "description": "Nível 1",
                "level": 1,
                "isLevelDetailed": True
            },
            "logo": {
                "id": 1,
                "url": "https://s3.amazonaws.com/prod-roadnet-integration/photos/driver/1602105808449"
            }
        },
        "hierarchicalLevel": {
            "id": "3"
        },
        "logo": {
            "url": "https://s3.amazonaws.com/prod-roadnet-integration/photos/driver/1602105808449"
        }
    }

    # Cabeçalhos da requisição
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YmlhbmNhQGRlc2FmaW86dDdOTVRyeUZiYjNTR1lDRA=='  # Ao informar usuario e senha no postman, ele gerou esse token. 

    }

    # Enviando a requisição POST
    response = requests.post(url_organization, headers=headers, data=json.dumps(organization))

    # Verificando a resposta da criação da organização
    if response.status_code == 200:
        response_data = response.json()
        print("Resposta da API:", response_data)
        print("Requisição bem-sucedida!")
    else:
        print(f"Erro na requisição: {response.status_code}")
        print("Detalhes do erro:", response.text)

    organization_id = response_data.get('id')

    print(f"O id da sua organização é: {organization_id}")
    #-------------------------------------------------Fim da criação da Organização---------------------------------------#

    # URL da API
    url_driverteam= 'http://desafio-api-trix.trixlog.com/driverteam'

    name_driverteam = input("Por favor, insira o nome do seu driverteam ")
    description_driverteam = input("Por favor, insira a descrição do seu driverteam ")

    driverteam = {
        "description": description_driverteam,   
        "drivers": [
        ],
        "filiationType": "INHERENT",
        "name": name_driverteam,
        "organization": {
            "id": organization_id
        },
        "representatives": [
            442
        ]
    }

    # Enviando a requisição POST
    response = requests.post(url_driverteam, headers=headers, data=json.dumps(driverteam))

    #Verificando a resposta da criação do DriverTeam
    if response.status_code == 200:
        response_data = response.json()
        print("Resposta da API:", response_data)
        print("Requisição bem-sucedida!")
    else:
        print(f"Erro na requisição: {response.status_code}")
        print("Detalhes do erro:", response.text)

    driverteam_id = response_data.get('id')

    print(f"O id do seu driverteam é: {driverteam_id}")

    #-------------------------------------------------Fim da criação do DriverTeam---------------------------------------# 

    #URL da API
    url_driver = 'http://desafio-api-trix.trixlog.com/driver'

    name_driver = input("Por favor, insira o nome do motorista que deseja cadastrar: ")
    login_driverteam = input("Por favor, insira o login que deseja cadastrar para o motorista: ")
    senha_driverteam = input("Por favor, insira a senha que deseja cadastrar para o motorista: ")
    driver_registration = input("Por favor, insira seu driver registration: ")
    driver_type = input("Por favor, insira o type do driver que deseja cadastrar, são eles: DRIVER, MECHANIC, VALET_PARKING, CANDIDATE: ")
    driver_birthDate = input("Por favor, insira a data de nascimento do motorista que deseja cadastrar: ")
    license = input("Por favor, insira o número da carteira de motorista: ")
    licenseRegister = input("Por favor, insira o número do registro da carteira de motorista: ")
    licenseExpedition = input("Por favor, insira a data de emissão da carteira de motorista, exemplo: 2000-01-15: ")
    licenseExpiration = input("Por favor, insira a data que irá expirar a carteira de motorista, exemplo: 2000-01-15: ")
    license_1 = ""
    license_2 = ""
    while True:
                            license_variavel = input("Qual habilitação você possui? A, B, C, D, E")
                                            
                            if license_variavel == "A":   
                                    license_1 = "A"
                                    break
                            elif license_variavel == "B":
                                    license_1 = "B"
                                    break
                            elif license_variavel == "C":
                                    license_1 = "C"
                                    break
                            elif license_variavel == "D":
                                    license_1 = "D"
                                    break
                            elif license_variavel == "E":
                                    license_1 = "E"
                                    break
                                    license_1 = "A"
                                    license_2 = "B"
                                    break
                            else:
                                print ("Resposta Inválida. Por favor, escolha A, B, C, D, E")
    driver_firstlicense = input("Por favor, insira a data da primeira habilitação, exemplo: 2000-01-15")
    driver = {
    "vehicles": [],
    "driverTeam": {
    "id": driverteam_id
    },
    "hiringType": "FIXED",
    "login": login_driverteam,    
    "name": name_driver,
    "password": senha_driverteam,
    "registration": driver_registration,
    "status": "ACTIVE",
    "statusDate": "2024-05-14T21:17:00.043Z",
    "type": driver_type,
    "birthDate": driver_birthDate,
    "license": license,
    "licenseRegister": licenseRegister,
    "licenseExpedition": licenseExpedition,
    "licenseExpiration": licenseExpiration,
    "licenses": [
        {
            "license": license_1
        }
    ],
    "firstLicense": "1990-05-07T03:00:00.000Z"
    }

    # Enviando a requisição POST
    response = requests.post(url_driver, headers=headers, data=json.dumps(driver))

    #Verificando a resposta da criação do Driver
    if response.status_code == 200:
        response_data = response.json()
        print("Resposta da API:", response_data)
        print("Requisição bem-sucedida!")
    else:
        print(f"Erro na requisição: {response.status_code}")
        print("Detalhes do erro:", response.text)

    driver_id = response_data.get('id')

    print(f"O id do seu driver é: {driver_id}")

    #-------------------------------------------------Fim da criação do Driver---------------------------------------#

    #URL da API
    url_group = 'http://desafio-api-trix.trixlog.com/group'

    group_name = input("Digite o nome do grupo que deseja criar: ")

    group = {
    "disabled": 0,
    "features": [],
    "isAdmin": 1,
    "name": group_name,
    "organization": {
        "id": organization_id
    } 
    }

    # Enviando a requisição POST
    response = requests.post(url_group, headers=headers, data=json.dumps(group))

    #Verificando a resposta da criação do Driver
    if response.status_code == 200:
        response_data = response.json()
        print("Resposta da API:", response_data)
        print("Requisição bem-sucedida!")
    else:
        print(f"Erro na requisição: {response.status_code}")
        print("Detalhes do erro:", response.text)

    group_id = response_data.get('id')

    print(f"O id do seu grupo é: {group_id}")

    #-------------------------------------------------Fim da criação do Group---------------------------------------#
elif action == "DELETE":
    entity_delete = input("Qual entidade deseja apagar?: ORGANIZATION, DRIVERTEAM, DRIVER OR GROUP? ")

    # Cabeçalhos da requisição
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YmlhbmNhQGRlc2FmaW86dDdOTVRyeUZiYjNTR1lDRA=='  # Ao informar usuario e senha no postman, ele gerou esse token. 

        }

    if entity_delete == "ORGANIZATION":
          id_delete = input("Digite o id da organização que deseja apagar: ")

          #URL DA API
          delete_organization = f'http://desafio-api-trix.trixlog.com/organization/{id_delete}'

          # Enviando a requisição DELETE
          response = requests.delete(delete_organization, headers=headers)

          #Verificando a resposta da criação do Driver
          if response.status_code == 200:
                response_data = response.json()
                print(f"Resposta da API:", {response_data})
                print("Requisição bem-sucedida!")
          else: 
                print(f"Erro na requisição: {response.status_code}")
                print("Detalhes do erro:", response.text)
    elif entity_delete == "DRIVERTEAM":
          id_delete = input("Digite o id do driverteam que deseja apagar: ")

          #URL DA API
          delete_driverteam = f'http://desafio-api-trix.trixlog.com/driverteam/{id_delete}'

          # Enviando a requisição DELETE
          response = requests.delete(delete_driverteam, headers=headers)

          #Verificando a resposta da criação do Driver
          if response.status_code == 200:
                response_data = response.json()
                print(f"Resposta da API:", {response_data})
                print("Requisição bem-sucedida!")
          else: 
                print(f"Erro na requisição: {response.status_code}")
                print("Detalhes do erro:", response.text)
    elif entity_delete == "DRIVER":
          id_delete = input("Digite o id do Driver que deseja apagar: ")

          #URL DA API
          delete_driver = f'http://desafio-api-trix.trixlog.com/driver/{id_delete}'

          # Enviando a requisição DELETE
          response = requests.delete(delete_driver, headers=headers)

          #Verificando a resposta da criação do Driver
          if response.status_code == 200:
                response_data = response.json()
                print(f"Resposta da API:", {response_data})
                print("Requisição bem-sucedida!")
          else: 
                print(f"Erro na requisição: {response.status_code}")
                print("Detalhes do erro:", response.text)
    elif entity_delete == "GROUP":
          id_delete = input("Digite o id do GROUP que deseja apagar: ")

          #URL DA API
          delete_group = f'http://desafio-api-trix.trixlog.com/group/{id_delete}'

          # Enviando a requisição DELETE
          response = requests.delete(delete_group, headers=headers)

          #Verificando a resposta da criação do Driver
          if response.status_code == 200:
                response_data = response.json()
                print(f"Resposta da API:", {response_data})
                print("Requisição bem-sucedida!")
          else: 
                print(f"Erro na requisição: {response.status_code}")
                print("Detalhes do erro:", response.text)
else:
      print("Valor informado é invalido, execute novamente o SCRIPT e preencha da forma recomendada")
