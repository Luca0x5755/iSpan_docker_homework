# docker 作業 / 大專框架

```sh
# 開發模式
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
