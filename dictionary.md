# English Premier League 24/25 Data Dictionary

This document describes the data columns available in the raw dataset (`data/raw/E0_2425.csv`) sourced from [football-data.co.uk](https://www.football-data.co.uk/).

## Match Information
| Column | Description |
|---|---|
| Div | League Division (E0 = English Premier League) |
| Date | Match Date (dd/mm/yyyy) |
| Time | match Time (Kick off) |
| HomeTeam | Home Team |
| AwayTeam | Away Team |
| Referee | Match Referee |

## Match Results & Stats
| Column | Description |
|---|---|
| FTHG | Full Time Home Team Goals |
| FTAG | Full Time Away Team Goals |
| FTR | Full Time Result (H=Home Win, D=Draw, A=Away Win) |
| HTHG | Half Time Home Team Goals |
| HTAG | Half Time Away Team Goals |
| HTR | Half Time Result (H=Home Win, D=Draw, A=Away Win) |
| HS | Home Team Shots |
| AS | Away Team Shots |
| HST | Home Team Shots on Target |
| AST | Away Team Shots on Target |
| HF | Home Team Fouls Committed |
| AF | Away Team Fouls Committed |
| HC | Home Team Corners |
| AC | Away Team Corners |
| HY | Home Team Yellow Cards |
| AY | Away Team Yellow Cards |
| HR | Home Team Red Cards |
| AR | Away Team Red Cards |

## Betting Odds (Examples)
| Column | Description |
|---|---|
| B365H | Bet365 home win odds |
| B365D | Bet365 draw odds |
| B365A | Bet365 away win odds |
| AvgH | Average home win odds from major bookmakers |
| AvgD | Average draw odds from major bookmakers |
| AvgA | Average away win odds from major bookmakers |

*Note: There are many other betting columns including Asian Handicaps (AH) and Over/Under results.*
