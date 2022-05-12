const path = require("path");
const { resolve } = require("path");
const { readdir } = require("fs").promises;
const fs = require("fs");
const { pascalCase } = require("pascal-case");

async function* getFiles(dir) {
  const dirents = await readdir(dir, { withFileTypes: true });
  for (const dirent of dirents) {
    const res = resolve(dir, dirent.name);
    if (dirent.isDirectory()) {
      yield* getFiles(res);
    } else {
      yield res;
    }
  }
}

let import_lines = [];
let component_lines = [];
let old_mother_comp_name = "";

(async () => {
  for await (const f of getFiles("src/components/from_mui")) {
    if (f.endsWith(".js")) {
      let import_path = f
        .replace(
          "/home/logic/_workspace/docusaurus-playlist/docusaurus_mui5_helloworld",
          "@site"
        )
        .replace(".js", "");

      let mother_dir_name = path.dirname(import_path).split("/").pop();
      let mother_comp_name = pascalCase(mother_dir_name);

      let import_comp_name = path.basename(f).replace(".js", "") + "Helloworld";
      let import_line = `import ${mother_comp_name}${import_comp_name} from "${import_path}";`;

      console.log({ test: mother_comp_name });
      import_lines.push(import_line);

      if (mother_comp_name !== old_mother_comp_name) {
        component_lines.push(`\n## ${mother_comp_name}\n`);
        old_mother_comp_name = mother_comp_name;
      }
      component_lines.push(
        `### ${import_comp_name}\n\n<${mother_comp_name}${import_comp_name} />\n`
      );
    }
  }

  fs.writeFileSync("./import_lines.tmp", import_lines.join("\n"), {
    encoding: "utf8",
  });

  fs.writeFileSync("./component_lines.tmp", component_lines.join("\n"), {
    encoding: "utf8",
  });
})();

console.log(pascalCase("string"));
