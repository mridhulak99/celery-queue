def init_app(app, conf_module="apis.config.conf"):
    app.config.from_object(conf_module)
