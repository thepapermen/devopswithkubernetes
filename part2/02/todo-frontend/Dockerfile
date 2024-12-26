# Based on script from here: https://bun.sh/guides/ecosystem/docker

FROM oven/bun:1.1.40-alpine AS base

WORKDIR /usr/src/app

FROM base AS install

RUN mkdir -p /temp/dev
COPY package.json bun.lockb /temp/dev/
RUN cd /temp/dev && bun install --frozen-lockfile

# install with --production (exclude devDependencies)
RUN mkdir -p /temp/prod
COPY package.json bun.lockb /temp/prod/
RUN cd /temp/prod && bun install --frozen-lockfile --production

FROM base AS prerelease
COPY --from=install /temp/dev/node_modules node_modules
COPY . .

ENV NODE_ENV=production
#RUN bun test
RUN bun run build-only

FROM busybox:stable
# From here: https://lipanski.com/posts/smallest-docker-image-static-website

WORKDIR /home/static

#COPY --from=install /temp/prod/node_modules node_modules
COPY --from=prerelease /usr/src/app/dist .
#COPY --from=prerelease /usr/src/app/package.json .

# Create a non-root user to own the files and run our server
RUN adduser -D static
USER static


# Copy the static website
# Use the .dockerignore file to control what ends up inside the image!
#COPY "static" .

# Run BusyBox httpd
CMD ["busybox", "httpd", "-f", "-v", "-p", "3000"]