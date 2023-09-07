from abc import ABC, ABCMeta, abstractmethod


class AbstClass(ABCMeta):
    pass


class MyMeta(type):
    def __new__(msc, name, bases, attrs, extra_kwargs):
        pass
