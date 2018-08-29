class Meta:
    def __getattr__(self, attr):
        print('Get attribute name: %s' % attr)

    def __setattr__(self, attr, value):
        print('Set attribute name: \'%s\' with value: \'%s\'' % (attr, value))
        self.__dict__[attr] = value


obj = Meta()
obj.person_name = 'Vadim'
