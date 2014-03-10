from resource import Resource


class Account(Resource):

    def __getattr__(self, name):
        # Allow to get quotas info
        if name in self.json_data["quotas"].keys():
            return self.json_data["quotas"][name]
        else:
            return Resource.__getattr__(self, name)
