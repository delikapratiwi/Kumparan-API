DELIKA PRATIWI
Delikapratiwi@gmail.com
0812-9642-0032
Kumparan - Backend Technical Assessment
---------------------------------------------------------------------------
API CRUD on NEWS and Topic
Routes :
- @app.route("/news", methods=["GET"])
- @app.route("/news", methods=["POST"])
- @app.route("/news/<id>", methods=["GET"])
- @app.route("/news/<id>", methods=["PUT"])
- @app.route("/news/<id>", methods=["DELETE"])

- @app.route("/topic", methods=["GET"])
- @app.route("/topic", methods=["POST"])
- @app.route("/topic/<id>", methods=["GET"])
- @app.route("/topic/<id>", methods=["PUT"])
- @app.route("/topic/<id>", methods=["DELETE"])

API filter by news status (0 = draft, 1 = publish, 2 = delete)
- @app.route("/news-filter-status/<status>", methods=["GET"])

API filter news	by its topics
- @app.route("/news-filter-topic/<topic>", methods=["GET"])