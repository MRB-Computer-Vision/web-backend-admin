import uuid
from app.main.models.user import User
from app.main.services.blacklist_service import save_token


class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'success': True,
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'success': False,
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'success': False,
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'success': False,
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'success': False,
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            auth_token = auth_token.replace('Bearer ', '')
            resp = User.decode_auth_token(auth_token)
            if isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'success': True,
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'is_admin': user.is_admin,
                        'created_at': str(user.created_at)
                    }
                }
                return response_object, 200
            response_object = {
                'success': False,
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'success': False,
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
