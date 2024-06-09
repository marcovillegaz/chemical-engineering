import numpy as np


class Reactor:
    def __init__(
        self,
        reactor_type,
        order_of_reaction,
        kinetic_constant,
        fractional_change=0,
    ):
        self.reactor_type = reactor_type
        self.order_of_reaction = order_of_reaction
        self.kinetic_constant = kinetic_constant
        self.fractional_change = fractional_change

    def residence_time(self):
        # This method will be overridden by child classes
        raise NotImplementedError("Subclasses should implement this method")

    def get_volume(
        self, volumetric_flow, output_conversion, input_concentration, input_conversion
    ):
        residence_time = self.residence_time(
            output_conversion,
            input_concentration,
            input_conversion,
        )
        volume = volumetric_flow * residence_time
        return volume

    def get_flow(self):
        pass


class PlugFlow(Reactor):
    def __init__(self, order_of_reaction, kinetic_constant):
        super().__init__("Plug Flow", order_of_reaction, kinetic_constant)

    def residence_time(self, concentration):
        # Rate law for plug flow reactor
        return self.kinetic_constant * (concentration**self.order_of_reaction)


class StirredTank(Reactor):
    def __init__(self, order_of_reaction, kinetic_constant):
        super().__init__("Stirred Tank", order_of_reaction, kinetic_constant)

    def residence_time(self, output_conversion, input_concentration, input_conversion):
        # Redifinition of variable for better manipulation
        n = self.order_of_reaction
        k = self.kinetic_constant
        Ca0 = input_concentration
        Xaf = output_conversion
        Xai = input_conversion

        return (Ca0 * (Xaf - Xai)) / (k * (Ca0 * (1 - Xaf)) ** n)


# Example usage
# plug_flow_reactor = PlugFlow(order_of_reaction=2, kinetic_constant=0.1)
my_reactor = StirredTank(order_of_reaction=0.25, kinetic_constant=0.05)

residence_time = my_reactor.residence_time(
    output_conversion=0.8,
    input_concentration=10,
    input_conversion=0.25,
)

volume = my_reactor.get_volume(
    volumetric_flow=10,
    output_conversion=0.8,
    input_concentration=10,
    input_conversion=0.25,
)

print(f"Residence time: {residence_time}")
print(f"Reactor volume: {volume}")
