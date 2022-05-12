const child_process = require("child_process");

child_process.execSync(
  "npx create-docusaurus@latest docusaurus-helloworld classic"
);

console.log("done");
