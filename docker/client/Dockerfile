FROM node:18 as development-stage

# SET WORKING DIRECTORY
WORKDIR /app_code

# Copy runtime script & make it executable
COPY /docker/client/runtime.sh /runtime.sh
RUN chmod +x /runtime.sh

# Copy Application code into a directory called `app_code`
COPY ./client /app_code

# Install ALL Dependencies
RUN yarn install

# ========================================
# ---- Executed at Container Runtime ----
# ========================================

# CMD commands get executed at container runtime!
CMD ["/runtime.sh"]

FROM node:18 as build-stage
# These values are hardcoded in as we would only reach this stage in a production environment
ENV APP_ENV=production
ENV VUE_APP_PUBLIC_BACKEND_URL=""
# SET WORKING DIRECTORY
WORKDIR /app_code

# Copy code and dependencies from development stage
COPY --from=development-stage /app_code /app_code

# Build for production
RUN yarn build

# Serve static files
FROM nginx as production-stage

# Copy over dist folder from build stage
COPY --from=build-stage /app_code/dist /app_code

# Copy over nginx configuration
COPY /docker/nginx/nginx.conf /etc/nginx/nginx.conf