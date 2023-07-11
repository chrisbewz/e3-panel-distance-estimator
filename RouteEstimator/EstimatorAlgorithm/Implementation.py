import numpy as np
import pandas as pd


class Estimator:
    __box_width = None
    __multiplier = None
    __horizontal_distance_sample = 150
    __gain_space_samples = None
    __horizontal_distance = None
    __upper_limit_percentage = 0.25
    __vertical_distance_values = None
    __direct_distance_values = None

    # Lista de valores para b de 0 -> 1500mm
    # 150 Samples gerados incluindo o ultimo valor "1500"mm
    # a -> 150 mm

    def __init__(self, width: float, kFactor: float, verticalValues, horizontalValues) -> None:

        self.__box_width = width
        self.__multiplier = kFactor
        self.__vertical_distance_values = np.asarray(verticalValues, float)
        self.__direct_distance_values = np.asarray(horizontalValues, float)

    def Evaluate(self, directDistance, vDistance, boxWidth, hDistance):

        # Apenas retorna a distância direta para n retornar erros
        if vDistance == 0 and hDistance == 0:
            return self.SingleAxisDistance(directDistance)

        if vDistance == 0 and hDistance != 0:
            return self.SingleAxisDistance(hDistance)

        if hDistance == 0 and vDistance != 0:
            return self.SingleAxisDistance(directDistance)

        vThreshold = vDistance / hDistance
        hThreshold = hDistance < (0.1 * vDistance)

        # Se o valor da distância horizontal for muito menor ao valor vertical vDist >> hDist
        # O ponto de conexão está próx a lateral da caixa
        # Considera-se somente o valor da distância direta = distancia vertical adicionada de uma fração do seu valor moderada pela variavel "limiting ratio"
        if hThreshold:
            return self.SingleAxisDistance(vDistance)

        # Se o valor da distância vertical for muito menor ao valor horizontal vDist << hDistance
        # O ponto de conexão está próx a altura "y" do chicote
        # Considera-se somente o valor da distância direta adicionada de uma fração do seu valor moderada pela variavel "limiting ratio"
        if vThreshold < .1:
            return directDistance + (self.__upper_limit_percentage * directDistance)

        denominator = (boxWidth - (2 * hDistance))
        raw_decreasing_factor = (vDistance / denominator)
        flattened_factor = np.exp(-raw_decreasing_factor)
        result = (directDistance * (1 + self.AdjustWeights(flattened_factor, self.__upper_limit_percentage)))
        return result

    def SingleAxisDistance(self, distance):
        return distance + (self.__upper_limit_percentage * distance)

    @staticmethod
    def AdjustWeights(self, currentFactor, limit):
        # Calcula a diff abosulta entre o valor atual e o limite especificado
        diff = np.absolute(limit - currentFactor)

        if currentFactor < limit:
            return currentFactor + diff
        else:
            return currentFactor - diff
