# Overview
Это пример установки GitLab в кластере миникуб.
### Установка
Инициализируем кластер миникуб и устанавливаем в кластер ингресс контроллер.
```bash
$ minikube start --cpus=3 --memory=8gb --disk-size=40gb --vm-driver=virtualbox
$ minikube addons enable ingress
```
Добавляем репозиторий чарта gitlab.
```bash
$ helm repo add gitlab https://charts.gitlab.io/
$ helm repo update
```
Забираем `values` чарта и редактируем, устанавливаем чарт (`sed` для osX)
```bash
$ helm get values gitlab > values.yaml
$ sed -i'.bac' -e "s|192.168.99.125|$(minikube ip)|g" values.yaml
$ helm install gitlab -f values.yaml gitlab/gitlab
```
Ждем когда гитлаб заинсталиться.

---
Увы не вышло, попробую со следующего [линка](https://docs.gitlab.com/charts/development/minikube/).

Ресурсы, 3 ядра, 6gb RAM. 
```bash
$ kubectl create namespace gitlab
$ curl --output values.yaml "https://gitlab.com/gitlab-org/charts/gitlab/raw/master/examples/values-minikube-minimum.yaml"
$ sed -i'.bac' -e "s|192.168.99.125|$(minikube ip)|g" values.yaml
$ helm repo add gitlab https://charts.gitlab.io/
$ helm repo update
$ helm upgrade --install gitlab gitlab/gitlab \
  --timeout 600s \
  -f values.yaml \
  --set global.hosts.domain=$(minikube ip).nip.io \
  --set global.hosts.externalIP=$(minikube ip)
```
Смотрим за подами...