/**
 * Block exa_get_contents calls to domains that always return 403/paywall.
 * 
 * Usage: pi -e pipeline/extensions/block-domains.ts
 */
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";

const BLOCKED = new Set([
  "reuters.com",
  "bloomberg.com",
  "axios.com",
  "cnbc.com",
  "politico.eu",
  "seekingalpha.com",
  "businessinsider.com",
  "wired.com",
  "business-standard.com",
  "datacenterdynamics.com",
  "etnownews.com",
  "archynewsy.com",
  "wccftech.com",
  "openai.com",
  "cybernews.com",
  "coindesk.com",
  "appleinsider.com",
  "aninews.in",
]);

function extractDomain(url: string): string {
  try {
    const hostname = new URL(url).hostname;
    return hostname.replace(/^www\./, "");
  } catch {
    return "";
  }
}

export default function (pi: ExtensionAPI) {
  pi.on("tool_call", async (event) => {
    if (event.tool !== "exa_get_contents") return;

    const urls: string[] = event.input?.urls ?? [];
    const blockedUrls = urls.filter((u) => BLOCKED.has(extractDomain(u)));

    if (blockedUrls.length > 0) {
      const domains = blockedUrls.map((u) => extractDomain(u));
      return {
        error: `Blocked domains: ${domains.join(", ")}. Use exa_search snippets instead — do not retry these URLs.`,
      };
    }
  });
}
