class Container{
    constructor(){
        this.posts = [
            {id: 1, user: 'Kostya', body: 'first message'},
            {id: 2, user: 'Vlad', body: 'second message'}
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