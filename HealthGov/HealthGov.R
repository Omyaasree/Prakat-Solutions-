---
title: "Case Study 2"
author: "Elle Lau, Omyaasree Balaji, Robsuny Muleta, Samantha Hernandez"
date: "2024-10-07"
output: html_document
---
  
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

QUESTION 1

```{r}
flights <- read.csv(file = "https://raw.githubusercontent.com/jdwilson4/Intro-Data-Science/refs/heads/master/Data/tweets.csv", header = F)
```