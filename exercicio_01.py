{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "exercicio-01.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP0rMbicUBgrejd1YzujT/A",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/angela-gabrielly/ser-347/blob/main/exercicio_01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercício 01. Usando o terminal interativo do Python, use o comando type(objeto) e descubra o tipo de dados dos seguintes objetos:\n",
        "\n",
        "1\n",
        "\n",
        "True\n",
        "\n",
        "5 / 2\n",
        "\n",
        "2.5\n",
        "\n",
        "False\n",
        "\n",
        "5 + 3j"
      ],
      "metadata": {
        "id": "jgOd-YmkgiYt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "type(1)\n",
        "#Resultado: <class 'int'>\n",
        "type(True)\n",
        "#Resultado: <class 'bool'>\n",
        "type(5/2)\n",
        "#Resultado: <class 'float'>\n",
        "type(2.5)\n",
        "#Resultado: <class 'float'>\n",
        "type(False)\n",
        "#Resultado: <class 'bool'>\n",
        "type(5+3j)\n",
        "#Resultado: <class 'complex'>"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gORSxypAgnMc",
        "outputId": "17be86cc-a1a9-4d87-f6b7-2507cf4359ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "complex"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    }
  ]
}