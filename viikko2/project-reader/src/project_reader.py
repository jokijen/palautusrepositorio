import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)
        
        # testiprinttausta:
        # print(content)
        # print(parsed_content)

        name = parsed_content["tool"]["poetry"]["name"]
        description = parsed_content["tool"]["poetry"]["description"]
        license_info = parsed_content["tool"]["poetry"]["license"]

        authors = parsed_content["tool"]["poetry"]["authors"]
        dependencies = parsed_content["tool"]["poetry"]["dependencies"]
        dependencies_list = list(dependencies.keys())
        dev_dependencies = parsed_content["tool"]["poetry"]["group"]["dev"]["dependencies"]
        dev_dependencies_list = list(dev_dependencies.keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license_info, authors, dependencies_list, dev_dependencies_list)
