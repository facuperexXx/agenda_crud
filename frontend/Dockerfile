# Etapa 1: Construcción
FROM node:20-alpine AS build
WORKDIR /frontend

# Desactivar SSL estrictamente para evitar el error de certificado
RUN npm config set strict-ssl false

COPY package*.json ./

# Instalamos TODAS las dependencias (incluyendo Vite)
RUN npm install

COPY . .

# Ahora Vite debería estar disponible en node_modules/.bin/vite
RUN npm run build

# Etapa 2: Servidor
FROM nginx:alpine
COPY --from=build /frontend/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]