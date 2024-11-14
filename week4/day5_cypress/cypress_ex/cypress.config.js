import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    baseUrl: "http://localhost:5174",
    supportFile: false,
    },
    viewportHeight:768,
    viewportWidth:1024,
    video:false
});
