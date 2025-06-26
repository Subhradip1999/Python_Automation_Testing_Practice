# Modular apis, wrapper of base_apis
from api_testing_framework.apis.base_api import BaseAPI

class PostAPI(BaseAPI):

    def get_all_posts(self):
        return self.get('/posts')

    def get_particular_post(self, post_id):
        return self.get(f'/posts/{post_id}')

    def create_post(self, data):
        return self.post('/posts', data=data)

    def update_post(self, post_id, data):
        return self.update(f'/posts/{post_id}', data=data)

    def delete_post(self, post_id):
        return self.delete(f'/posts/{post_id}')
