class Project:
    def __init__(self, name, description, license_info, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license_info = license_info
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        #return ", ".join(dependencies) if len(dependencies) > 0 else "-"
        return "\n".join(f"- {dep}" for dep in dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license_info or '-'}"
            f"\n\nAuthors: \n{self._stringify_dependencies(self.authors)}"
            f"\n\nDependencies: \n{self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: \n{self._stringify_dependencies(self.dev_dependencies)}"
        )
