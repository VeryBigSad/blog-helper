<template>
    <div class="blog-post-preview" @click="blogPostPreviewClick()">
        <h3>{{ blogPost.title }}</h3>
        <p>{{ blogPost.description }}</p>
    </div>
</template>

<script>
export default {
    name: "BlogPostPreviewComponent",
    props: {
        blogPost: {
            type: Object,
            required: true,
        },
    },
    methods: {
        blogPostPreviewClick() {
            console.log(this.blogPost)
            this.$router.push(`/blog/${this.blogPost.id}`);
        },
    }
};
</script>

<style scoped>
.blog-post-preview {
    border: 1px solid black;
    padding: 10px;
    margin: 10px;
}

.blog-post-preview:hover {
    background-color: #f5f5f5;
    cursor: pointer;
}

</style>
