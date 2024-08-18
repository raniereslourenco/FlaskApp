from flask import Flask, request, jsonify
from models.task import Task

#__name__ = "__main__"
app = Flask(__name__)

#CRUD - Create, Read, Update e Delete
#Tabela: Tarefa

#1ª Fase - Listas
tasks = []

#criar uma nova tarefa
taskIdControl = 1
@app.route("/tasks", methods=["POST"])
def createTask():
    global taskIdControl
    data = request.get_json()
    new_task = Task(id=taskIdControl,title=data.get("title"), description=data.get("description", ""))
    taskIdControl += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"Nova tarefa criada com sucesso", "id": new_task.id})

#Ler/recuperar as tarefas
@app.route("/tasks", methods=["GET"])
def getTasks():
    '''
    Modo 1 de resolução do caso
    taskList = []
    for task in tasks:
        taskList.append(task.to_dict())
    '''
    taskList = [task.to_dict() for task in tasks]
    output = {
        "task":taskList,
        "total_tasks": len(taskList)
    }
    return jsonify(output)

#ler/recuperar uma tarefa especifica
@app.route("/tasks/<int:id>", methods=["GET"])
def getTask(id):
    #task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"Message":"Não foi possível encontrar a atividade"}), 404

#alterar task
@app.route("/tasks/<int:id>", methods=["PUT"])
def updTask(id):
    
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message":"Tarefa atualizada com sucesso"})

#deletar tarefa
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delTask(id):
    task = None
    for t in tasks:
        if t.id ==id:
            task = t
            break

    if not task:
        return jsonify({"message":"Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message":"Tarefa deletada com sucesso!"})
#rodar o programa
if __name__ == "__main__": #desenvolvimento local
    app.run(debug=True)