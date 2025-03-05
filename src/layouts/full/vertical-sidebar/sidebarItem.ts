import {
  LayoutDashboardIcon, BorderAllIcon,
  AlertCircleIcon,
  CircleDotIcon,
  BoxMultiple1Icon,
  LoginIcon, MoodHappyIcon, ApertureIcon, UserPlusIcon
} from 'vue-tabler-icons';

export interface menu {
  header?: string;
  title?: string;
  icon?: any;
  to?: string;
  chip?: string;
  BgColor?: string;
  chipBgColor?: string;
  chipColor?: string;
  chipVariant?: string;
  chipIcon?: string;
  children?: menu[];
  disabled?: boolean;
  type?: string;
  subCaption?: string;
}

const sidebarItem: menu[] = [
  { header: 'Home' },
  {
      title: 'Incio',
      icon: LayoutDashboardIcon,
      BgColor: 'primary',
      to: '/'
  },
  { header: 'Componentes' },
  {
      title: "Temperatura",
      icon: AlertCircleIcon,
      BgColor: 'primary',
      to: "/ui/alerts",
  },
  {
      title: "Humedad",
      icon: CircleDotIcon,
      BgColor: 'primary',
      to: "/ui/buttons",
  },
  
];

const userRole = localStorage.getItem('userRole');

if (userRole === 'admin') {
  sidebarItem.push(
      { header: 'Auth' }, // Agrega el encabezado solo si el usuario es admin
      {
          title: 'Usuarios',
          icon: UserPlusIcon,
          BgColor: 'primary',
          to: '/ui/tables'
      }
  );
}

export default sidebarItem;
/*
export interface menu {
  header?: string;
  title?: string;
  icon?: any;
  to?: string;
  chip?: string;
  BgColor?: string;
  chipBgColor?: string;
  chipColor?: string;
  chipVariant?: string;
  chipIcon?: string;
  children?: menu[];
  disabled?: boolean;
  type?: string;
  subCaption?: string;
}

const sidebarItem: menu[] = [
  { header: 'Home' },
  {
    title: 'Incio',
    icon: LayoutDashboardIcon,
    BgColor: 'primary',
    to: '/'
  },
  { header: 'Componentes' },
  {
    title: "Temperatura",
    icon: AlertCircleIcon,
    BgColor: 'primary',
    to: "/ui/alerts",
    
  },
  {
    title: "Humedad",
    icon: CircleDotIcon,
    BgColor: 'primary',
    to: "/ui/buttons",
  },
  /*{
    title: "Cards",
    icon: BoxMultiple1Icon,
    BgColor: 'primary',
    to: "/ui/cards",
  },
  {
    title: "Tables",
    icon: BorderAllIcon,
    BgColor: 'primary',
    to: "/ui/tables",
  },*/
  
  { header: 'Auth' }
  /*
  {
    title: 'Login',
    icon: LoginIcon,
    BgColor: 'primary',
    to: '/auth/login'
},
{
    title: 'Registar',
    icon: UserPlusIcon,
    BgColor: 'primary',
    to: '/auth/register'
},
{
  title: 'Usuarios',
  icon: UserPlusIcon,
  BgColor: 'primary',
  to: '/auth/register'
},*/
/*{
  title: 'Usuarios',
  icon: UserPlusIcon,
  BgColor: 'primary',
  to: '/ui/tables'
},*/
/*{ header: 'Extra' },
{
    title: 'Icons',
    icon: MoodHappyIcon,
    BgColor: 'primary',
    to: '/icons'
},
{
    title: 'Sample Page',
    icon: ApertureIcon,
    BgColor: 'primary',
    to: '/sample-page'
},*/
/*
];
const userRole = localStorage.getItem('userRole');

if (userRole === 'admin') {
    sidebarItem.push({
        title: 'Usuarios',
        icon: UserPlusIcon,
        BgColor: 'primary',
        to: '/ui/tables'
    });
}

export default sidebarItem;
*/