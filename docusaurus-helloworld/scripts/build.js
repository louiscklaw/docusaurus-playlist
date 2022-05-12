const child_process = require("child_process");

child_process.execSync("yarn --dev");
child_process.execSync("yarn build");
child_process.execSync("rm -rf ../docs");
child_process.execSync("mkdir -p ../docs");
child_process.execSync("cp -R build/* ../docs");
