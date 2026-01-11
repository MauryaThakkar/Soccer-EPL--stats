# EPL Data Cheat Sheet

This reference guide explains the columns found in the `E0` (English Premier League) dataset from [football-data.co.uk](https://www.football-data.co.uk/).

## 1. Match Information
| Column | Description |
|---|---|
| **Div** | League Division (E0 = English Premier League) |
| **Date** | Match Date (dd/mm/yyyy) |
| **Time** | Kick-off Time |
| **HomeTeam** | Home Team Name |
| **AwayTeam** | Away Team Name |
| **Referee** | Match Referee Name |

## 2. Match Results
| Column | Description |
|---|---|
| **FTHG** | **F**ull **T**ime **H**ome **G**oals |
| **FTAG** | **F**ull **T**ime **A**way **G**oals |
| **FTR** | **F**ull **T**ime **R**esult (H=Home Win, D=Draw, A=Away Win) |
| **HTHG** | **H**alf **T**ime **H**ome **G**oals |
| **HTAG** | **H**alf **T**ime **A**way **G**oals |
| **HTR** | **H**alf **T**ime **R**esult (H=Home Win, D=Draw, A=Away Win) |

## 3. Match Statistics
| Column | Description |
|---|---|
| **HS** | Home Team Shots |
| **AS** | Away Team Shots |
| **HST** | Home Team Shots on Target |
| **AST** | Away Team Shots on Target |
| **HF** | Home Team Fouls Committed |
| **AF** | Away Team Fouls Committed |
| **HC** | Home Team Corners |
| **AC** | Away Team Corners |
| **HY** | Home Team Yellow Cards |
| **AY** | Away Team Yellow Cards |
| **HR** | Home Team Red Cards |
| **AR** | Away Team Red Cards |

## 4. Betting Odds (Key Providers)
*Odds for Home Win (H), Draw (D), and Away Win (A)*

| Provider | Code Prefix | Example Columns |
|---|---|---|
| **Bet365** | `B365` | `B365H`, `B365D`, `B365A` |
| **BetWin** | `BW` | `BWH`, `BWD`, `BWA` |
| **Interwetten** | `IW` | `IWH`, `IWD`, `IWA` |
| **Pinnacle** | `PS` | `PSH`, `PSD`, `PSA` |
| **William Hill**| `WH` | `WHH`, `WHD`, `WHA` |
| **VC Bet** | `VC` | `VCH`, `VCD`, `VCA` |
| **Market Max** | `Max` | `MaxH`, `MaxD`, `MaxA` |
| **Market Avg** | `Avg` | `AvgH`, `AvgD`, `AvgA` |

## 5. Goals Betting (Over/Under 2.5)
| Column | Description |
|---|---|
| **[Provider]>2.5** | Odds for Over 2.5 Goals (e.g., `B365>2.5`) |
| **[Provider]<2.5** | Odds for Under 2.5 Goals (e.g., `B365<2.5`) |

## 6. Asian Handicap Betting
| Column | Description |
|---|---|
| **AHh** | Asian Handicap size (e.g., -0.5, +1.0) |
| **[Provider]AHH** | Odds for Home Team to beat the handicap |
| **[Provider]AHA** | Odds for Away Team to beat the handicap |

## 7. Closing Odds
*Columns containing 'C' (e.g., `B365CH`) denote the closing odds just before kick-off, as opposed to opening/pre-match odds.*

| Example | Description |
|---|---|
| **B365CH** | Bet365 Closing Home Win Odds |
| **MaxCH** | Market Maximum Closing Home Win Odds |
| **AvgC>2.5**| Market Average Closing Over 2.5 Goals Odds |
