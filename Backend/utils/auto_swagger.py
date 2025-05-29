from drf_yasg.utils import swagger_auto_schema

def auto_swagger(request, response):
    def class_decorator(viewset_class):
        for method_name in ['create', 'update', 'partial_update', 'list', 'retrieve']:
            if hasattr(viewset_class , method_name):
                original = getattr(viewset_class , method_name)
                kwargs = {'responses': {200: response}}
                if method_name in ['create', 'update', 'partial_update'] and request is not None:
                    kwargs['request_body'] = request
                decorated = swagger_auto_schema(**kwargs)(original)
                setattr(viewset_class , method_name, decorated)
        return viewset_class 
    return class_decorator