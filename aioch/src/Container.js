class Container{
    constructor(){
        this.posts = [
            {user: 'Kostya', body: 'first message'},
            {user: 'Vlad', body: 'second message'}
        ];
    }

    getPosts(){
        return this.posts;
    }
    
    addPost(user, body){
        this.posts.push({user, body})
        console.log(this.posts);
    }
}

export default Container;