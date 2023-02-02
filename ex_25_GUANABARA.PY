"""Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome."""

nm = str(input("Informe seu nome: ")).strip().upper()
print(f"Voce tem Silva no seu nome? {('SILVA') in nm}")