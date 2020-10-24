export default async (url) => {
    const listArticleRes = await fetch(url);
    return await listArticleRes.json();
}