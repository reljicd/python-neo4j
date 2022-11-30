from python_neo4j.session.session import db


def test_session():
    hello = 'Hello World'
    with db().begin_transaction() as tx:
        result = tx.run("CREATE (a:Greeting) "
                        f"SET a.message = '{hello}' "
                        "RETURN a.message + ', from node ' + id(a)")
        returned_hello = result.single()[0]
    assert hello in returned_hello
