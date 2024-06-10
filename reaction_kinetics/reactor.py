import numpy as np
import scipy.integrate as integrate


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

    def residence_time(
        self, output_conversion, input_concentration, input_conversion, epsilon
    ):
        # Redifinition of variable for better manipulation
        n = self.order_of_reaction
        k = self.kinetic_constant
        Ca0 = input_concentration
        Xaf = output_conversion
        Xai = input_conversion

        integral, _ = integrate.quad(
            lambda Xa: ((1 + epsilon * Xa) / (1 - Xa)) ** n,
            Xai,
            Xaf,
        )

        return (1 / (k * Ca0 ** (n - 1))) * integral


class StirredTank(Reactor):
    def __init__(self, order_of_reaction, kinetic_constant):
        super().__init__("Stirred Tank", order_of_reaction, kinetic_constant)

    def residence_time(
        self, output_conversion, input_concentration, input_conversion, epsilon
    ):
        # Redifinition of variable for better manipulation
        n = self.order_of_reaction
        k = self.kinetic_constant
        Ca0 = input_concentration
        Xaf = output_conversion
        Xai = input_conversion

        return (1 / (k * Ca0 ** (n - 1))) * (
            ((Xaf * ((1 + epsilon * Xaf) ** n) - Xai)) / ((1 - Xaf) ** n)
        )
