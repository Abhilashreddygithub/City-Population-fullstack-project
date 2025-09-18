FROM node:18

WORKDIR /app

RUN pwd

COPY package.json .

COPY public ./public

COPY code ./src

COPY . .

RUN npm install

RUN npm run build

CMD ["npx", "serve", "-s", "build", "-l", "3000"]