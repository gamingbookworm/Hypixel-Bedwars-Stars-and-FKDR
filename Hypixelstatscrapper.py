import hypixel
import time
import csv
import sys
import subprocess
import os
import webbrowser
import ctypes
import flask
import openpyxl
from flask import request, jsonify

API_KEYS = ['YourAPI']
hypixel.setKeys(API_KEYS)

workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "Player Stats"
worksheet.append(["Player", "Rank", "Level", "Stars", "Wins", "Beds", "SoloKDR", "SoloFKDR", "SoloGames", "DuoKDR", "DuoFKDR", "DuoGames", "TrioKDR", "TrioFKDR", "TrioGames", "QuadKDR", "QuadFKDR", "QuadGames", "FourKDR", "FourFKDR", "FourGames", "KDR", "FKDR", "Games"])

usernames = ["player1", "player2"]

for username in usernames:
  Player = hypixel.Player(username)
  print('')
  print(Player)

  #HYPIXEL STATS
  Name = Player.getName()
  Rank = Player.getRank()['rank']
  Level = Player.getLevel()

  #BEDWARS STATS
  def getInfo(json, param):
    try:
      return int(json['achievements']['bedwars_level'])
    except:
      return 0
  Stars = getInfo(Player.JSON, "achievements""bedwars_level")

  def getInfo(json, param):
    try:
      return int(json['achievements']['bedwars_wins'])
    except:
      return 0
  Wins = getInfo(Player.JSON, "achievements""bedwars_wins")

  def getInfo(json, param):
    try:
      return int(json['achievements']['bedwars_beds'])
    except:
      return 0
  Beds = getInfo(Player.JSON, "achievements""bedwars_beds")

  def getInfo(json, param):
    try:
      return int(json['stats']['Bedwars'][param])
    except:
      return 0

  SoloKDR = getInfo(Player.JSON, "eight_one_kills_bedwars")/max(getInfo(Player.JSON, "eight_one_deaths_bedwars"), 1)
  SoloFKDR = getInfo(Player.JSON, "eight_one_final_kills_bedwars")/max(getInfo(Player.JSON, "eight_one_final_deaths_bedwars"), 1)
  SoloGames = getInfo(Player.JSON, "eight_one_games_played_bedwars")
  
  DuoKDR = getInfo(Player.JSON, "eight_two_kills_bedwars")/max(getInfo(Player.JSON, "eight_two_deaths_bedwars"), 1)
  DuoFKDR = getInfo(Player.JSON, "eight_two_final_kills_bedwars")/max(getInfo(Player.JSON, "eight_two_final_deaths_bedwars"), 1)
  DuoGames = getInfo(Player.JSON, "eight_two_games_played_bedwars")

  TrioKDR = getInfo(Player.JSON, "four_three_kills_bedwars")/max(getInfo(Player.JSON, "four_three_deaths_bedwars"), 1)
  TrioFKDR = getInfo(Player.JSON, "four_three_final_kills_bedwars")/max(getInfo(Player.JSON, "four_three_final_deaths_bedwars"), 1)
  TrioGames = getInfo(Player.JSON, "four_three_games_played_bedwars")

  QuadKDR = getInfo(Player.JSON, "four_four_kills_bedwars")/max(getInfo(Player.JSON, "four_four_deaths_bedwars"), 1)
  QuadFKDR = getInfo(Player.JSON, "four_four_final_kills_bedwars")/max(getInfo(Player.JSON, "four_four_final_deaths_bedwars"), 1)
  QuadGames = getInfo(Player.JSON, "four_four_games_played_bedwars")

  FourKDR = getInfo(Player.JSON, "four_two_kills_bedwars")/max(getInfo(Player.JSON, "four_two_deaths_bedwars"), 1)
  FourFKDR = getInfo(Player.JSON, "four_two_final_kills_bedwars")/max(getInfo(Player.JSON, "four_two_final_deaths_bedwars"), 1)
  FourGames = getInfo(Player.JSON, "four_two_games_played_bedwars")

  KDR = getInfo(Player.JSON, "kills_bedwars")/max(getInfo(Player.JSON, "deaths_bedwars"), 1)
  FKDR = getInfo(Player.JSON, "final_kills_bedwars")/max(getInfo(Player.JSON, "final_deaths_bedwars"), 1)
  Games = getInfo(Player.JSON, "games_played_bedwars")

  worksheet.append([Name, Rank, Level, Stars, Wins, Beds, SoloKDR, SoloFKDR, SoloGames, DuoKDR, DuoFKDR, DuoGames, TrioKDR, TrioFKDR, TrioGames, QuadKDR, QuadFKDR, QuadGames, FourKDR, FourFKDR, FourGames, KDR, FKDR, Games])

filepath = r"C:\Users\natal\Documents\output.xlsx"  # Replace 'user' with your actual user name
workbook.save(filepath)
