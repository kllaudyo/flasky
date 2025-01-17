import os
from app import create_app, db
from app.models import User, Role, Permission
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_ENV') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        User=User,
        Role=Role,
        Permission=Permission
    )


@app.cli.command()
def test():
    """Exceuta testes"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
