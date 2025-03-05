/*Recent Transaction*/
type recentTrans = {
    title: string;
    subtitle: string;
    textcolor: string;
    boldtext: boolean;
    line: boolean;
    link: string;
    url: string;
};

/*product performance*/
type productPerformanceType = {
    id: number;
    name: string;
    post: string;
    pname: string;
    status: string;
    statuscolor: string;
    budget: string;
};


export type { recentTrans, productPerformanceType}