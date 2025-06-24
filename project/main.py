from project.utils.parser import parse_natural_input_to_travel_request

def main():
    entrada = input("Introduce tu petición de viaje:\n")
    parsed = parse_natural_input_to_travel_request(entrada)
    print("\nResultado estructurado:")
    print(parsed.model_dump())

if __name__ == "__main__":
    main()