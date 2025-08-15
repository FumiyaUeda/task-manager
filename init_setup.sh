#!/bin/bash
set -e

# パッケージ更新
sudo apt update && sudo apt upgrade -y

# 必須ツール
sudo apt install -y git curl build-essential

# タイムゾーン設定
sudo timedatectl set-timezone Asia/Tokyo

# スワップ追加（1GB）
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab





