import os
import ast
import astor
from itertools import combinations


class MutationTransformer(ast.NodeTransformer):
    def __init__(self, changes):
        self.changes = changes

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name) and node.targets[0].id in self.changes:
            new_value = ast.parse(self.changes[node.targets[0].id]).body[0].value
            return ast.copy_location(ast.Assign(targets=node.targets, value=new_value), node)
        return node


def mutate_class(class_code, changes, output_file):
    tree = ast.parse(class_code)
    transformer = MutationTransformer(changes)
    transformed_tree = transformer.visit(tree)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(astor.to_source(transformed_tree))


# Configuración base segura
secure_config_code = '''
class CORSConfig:
    ORIGINS = ['http://example.com', 'http://another-example.com']
    METHODS = ['GET', 'POST', 'PUT', 'DELETE']
    ALLOW_HEADERS = ['Authorization', 'Content-Type']
    SUPPORTS_CREDENTIALS = False
    MAX_AGE = 3600
    SEND_WILDCARD = False
    AUTOMATIC_OPTIONS = False
    VARY_HEADER = True

class AppConfig:
    API_KEY = "your_secret_api_key"
'''

# Valores vulnerables
vulnerable_changes = {
    'CORSConfig': [
        {'ORIGINS': "['*']"},
        {'METHODS': "['*']"},
        {'ALLOW_HEADERS': "['*']"},
        {'SUPPORTS_CREDENTIALS': "True"},
        {'MAX_AGE': "86400"},
        {'SEND_WILDCARD': "True"},
        {'AUTOMATIC_OPTIONS': "True"},
        {'VARY_HEADER': "False"}
    ],
    'AppConfig': [
        {'API_KEY': '""'}
    ]
}


def generate_individual_mutations(config_code, class_name, changes, output_prefix):
    for i, change in enumerate(changes):
        output_file = f'mutants/{output_prefix}_mutation_{i + 1}.py'
        mutate_class(config_code, change, output_file)


def generate_combined_mutations(config_code, class_name, changes, output_prefix):
    num_changes = len(changes)
    for r in range(2, num_changes + 1):
        for combo in combinations(range(num_changes), r):
            combined_changes = {}
            for idx in combo:
                combined_changes.update(changes[idx])
            output_file = f'mutants/{output_prefix}_mutation_combined_{"_".join(map(str, combo))}.py'
            mutate_class(config_code, combined_changes, output_file)


# Crear mutaciones individuales y combinadas para cada clase
for class_name, changes in vulnerable_changes.items():
    generate_individual_mutations(secure_config_code, class_name, changes, class_name.lower())
    generate_combined_mutations(secure_config_code, class_name, changes, class_name.lower())
