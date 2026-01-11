library(tidyverse)
library(ggplot2)

# ==========================================
# CONFIGURATION
# ==========================================
RAW_PATH <- "data/raw/E0_2425.csv"
DATA_URL <- "https://www.football-data.co.uk/mmz4281/2122/E0.csv"

# 1. Load Data
if (!file.exists(RAW_PATH)) {
  message("Downloading data...")
  df <- read_csv(DATA_URL)
  write_csv(df, RAW_PATH)
} else {
  df <- read_csv(RAW_PATH)
}

# 2. Exploratory Data Analysis (EDA)
# Question: Is there a significant Home Advantage in terms of Goal Difference?

df <- df %>%
  mutate(GoalDiff = FTHG - FTAG)

# Visualization: Distribution of Goal Differences
p1 <- ggplot(df, aes(x = GoalDiff)) +
  geom_density(fill = "blue", alpha = 0.3) +
  geom_vline(aes(xintercept = mean(GoalDiff, na.rm = TRUE)), color = "red", linetype = "dashed") +
  labs(title = "Distribution of Match Goal Differences (Home - Away)",
       subtitle = paste("Mean GD:", round(mean(df$GoalDiff, na.rm=TRUE), 3)),
       x = "Goal Difference (Positive = Home Win)",
       y = "Density") +
  theme_minimal()

print(p1)
# ggsave("../../reports/goal_diff_distribution.png")

# 3. Statistical Hypothesis Testing
# Null Hypothesis (H0): Mean Goal Difference is 0 (No Home Advantage)
# Alternative Hypothesis (H1): Mean Goal Difference != 0

t_test_result <- t.test(df$GoalDiff, mu = 0)

print("T-test Results for Home Advantage:")
print(t_test_result)

if(t_test_result$p.value < 0.05) {
  print("Result: Statistically Significant Home Advantage found.")
} else {
  print("Result: No significant Home Advantage found.")
}

# 4. Advanced: Compare top teams vs rest
top_6 <- c("Man City", "Liverpool", "Chelsea", "Tottenham", "Arsenal", "Man United")

df <- df %>%
  mutate(IsTop6 = ifelse(HomeTeam %in% top_6, "Top 6", "Other"))

# Boxplot of Shots on Target by Team Tier
p2 <- ggplot(df, aes(x = IsTop6, y = HST, fill = IsTop6)) +
  geom_boxplot() +
  labs(title = "Home Shots on Target: Top 6 vs Others",
       y = "Shots on Target (Home)") +
  theme_bw()

print(p2)
