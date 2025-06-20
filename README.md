# docker 作業 / 大專框架

## 檔案目錄

```sh
.
│  .gitignore              # Git 忽略規則
│  app.py                  # Python Flask 主應用程式
│  docker-compose.yml      # Docker Compose 開發環境設定
│  docker-compose.prod.yml # Docker Compose 生產環境設定
│  Dockerfile              # Docker 映像檔建置設定
│  generate-cert.sh        # 產生 SSL 憑證的 Shell 腳本
│  init.sql                # 初始化資料庫 SQL 腳本
│  README.md               # 專案說明文件
│  requirements.txt        # Python 相依套件列表
│
└─nginx/
    │  nginx.conf          # NGINX 設定檔
```

## 開發模式

```sh
docker-compose up
```

## 本地開發需更改路徑，改成專案位置

```yml
# docker-compose.yml
  flask:
    volumes:
      - D:/iSpan_docker_homework:/app
```

## 使用自簽憑證

1. 生產模式使用
2. 在ubuntu中執行 generate-cert.sh
3. 將產生出來的`certs`資料夾放置在專案內的`nginx`資料夾內

```sh
# 建立自簽憑證
source generate-cert.sh

# 生產模式
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```
