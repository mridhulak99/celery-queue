import connexion

def create_app():
    connexion_app = connexion.App('__name__',
                            specification_dir='apis/swagger/')
    
    connexion_app.add_api('root.yaml',
                validate_responses=True,
                strict_validation=True,
                pass_context_arg_name='request')
    
    flask_app = connexion_app.app

    import apis.config as config
    config.init_app(flask_app)

    import apis.utils as utils
    utils.init_app(flask_app)

    return flask_app
    
    

