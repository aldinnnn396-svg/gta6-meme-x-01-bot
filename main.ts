import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

function main(): void {
  const botDir: string = process.env.MAKEFUN_BOT_DIR || "/bot";
  const outDir: string = process.env.MAKEFUN_OUTPUT_DIR || "/output";
  mkdirSync(outDir, { recursive: true });
  const srcPath: string = join(botDir, "POST.json");
  const dstPath: string = join(outDir, "POST.json");
  copyFileSync(srcPath, dstPath);
}

main();
