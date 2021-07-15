export default {
  repository: "", // project repo
  docsRepository: "", // docs repo
  branch: "main", // branch of docs
  path: "/", // path of docs
  titleSuffix: " – Approximate Computing Tool",
  nextLinks: true,
  prevLinks: true,
  search: true,
  customSearch: null, // customizable, you can use algolia for example
  darkMode: true,
  footer: false,
  footerText: ``,
  footerEditOnGitHubLink: false, // will link to the docs repo
  logo: (
    <span className="mr-2 font-extrabold hidden md:inline">
      Approximate Computing Tool
    </span>
  ),
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta
        name="description"
        content="Approximate Computing Tool Documentation"
      />
      <meta name="og:title" content="Approximate Computing Tool" />
    </>
  ),
};
